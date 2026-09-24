"""
Project ASMA - Private Income OS
Author: Md Subhan Pasha
Dedicated to: Asma

Module: crypto_vault.py
Purpose: Local-First AES-256-GCM Encryption Vault & SHA-256 Cryptographic Verification
Zero telemetry, local storage only.
"""

import os
import hashlib
import secrets
from pathlib import Path
from typing import Union
from dotenv import load_dotenv

# Load environment secrets
load_dotenv()

DATA_DIR = Path(__file__).parent / "data"
KEY_FILE = DATA_DIR / "vault.key"


class CryptoVault:
    """
    Military-grade AES-256-GCM Vault for local data privacy.
    Ensures zero cloud leakage and strict local integrity verification.
    """

    def __init__(self, key_bytes: bytes = None):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.key = key_bytes or self._load_or_generate_key()

    def _load_or_generate_key(self) -> bytes:
        """Loads AES-256 key from .env or local keyfile, or securely generates one."""
        env_key = os.getenv("AES_ENCRYPTION_KEY", "").strip()
        if env_key:
            try:
                # Expect 64 hex chars = 32 bytes (256 bits)
                key = bytes.fromhex(env_key)
                if len(key) == 32:
                    return key
            except ValueError:
                pass

        if KEY_FILE.exists():
            try:
                key = KEY_FILE.read_bytes()
                if len(key) == 32:
                    return key
            except Exception:
                pass

        # Generate fresh 256-bit (32-byte) key
        key = secrets.token_bytes(32)
        try:
            KEY_FILE.write_bytes(key)
            # Try to update .env if present
            env_path = Path(__file__).parent / ".env"
            if env_path.exists():
                content = env_path.read_text(encoding="utf-8")
                if "AES_ENCRYPTION_KEY=" in content:
                    lines = content.splitlines()
                    new_lines = []
                    for line in lines:
                        if line.startswith("AES_ENCRYPTION_KEY="):
                            new_lines.append(f"AES_ENCRYPTION_KEY={key.hex()}")
                        else:
                            new_lines.append(line)
                    env_path.write_text("\n".join(new_lines), encoding="utf-8")
        except Exception:
            pass

        return key

    def encrypt_bytes(self, plaintext: bytes) -> bytes:
        """
        Encrypts plaintext bytes using AES-256-GCM.
        Output format: [12-byte Nonce] + [Ciphertext + 16-byte Auth Tag]
        """
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM

        aesgcm = AESGCM(self.key)
        nonce = secrets.token_bytes(12)  # 96-bit standard nonce for GCM
        ciphertext = aesgcm.encrypt(nonce, plaintext, None)
        return nonce + ciphertext

    def decrypt_bytes(self, encrypted_data: bytes) -> bytes:
        """
        Decrypts AES-256-GCM payload.
        """
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM

        if len(encrypted_data) < 28:
            raise ValueError("Encrypted data payload is too short or corrupted.")

        nonce = encrypted_data[:12]
        ciphertext = encrypted_data[12:]
        aesgcm = AESGCM(self.key)
        return aesgcm.decrypt(nonce, ciphertext, None)

    def encrypt_string(self, text: str) -> str:
        """Encrypts UTF-8 string and returns hex-encoded ciphertext."""
        raw = text.encode("utf-8")
        enc = self.encrypt_bytes(raw)
        return enc.hex()

    def decrypt_string(self, hex_text: str) -> str:
        """Decrypts hex-encoded AES-256-GCM ciphertext to UTF-8 string."""
        raw = bytes.fromhex(hex_text.strip())
        dec = self.decrypt_bytes(raw)
        return dec.decode("utf-8")

    def encrypt_file(self, input_file: Union[str, Path], output_file: Union[str, Path] = None) -> Path:
        """Encrypts an entire file to a secure .enc file."""
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"File not found: {input_path}")

        out_path = Path(output_file) if output_file else input_path.with_suffix(input_path.suffix + ".enc")
        data = input_path.read_bytes()
        encrypted = self.encrypt_bytes(data)
        out_path.write_bytes(encrypted)
        return out_path

    def decrypt_file(self, enc_file: Union[str, Path], output_file: Union[str, Path] = None) -> Path:
        """Decrypts a .enc file to its original content."""
        enc_path = Path(enc_file)
        if not enc_path.exists():
            raise FileNotFoundError(f"Encrypted file not found: {enc_path}")

        if output_file:
            out_path = Path(output_file)
        else:
            out_path = enc_path.with_suffix("")  # strips .enc

        enc_data = enc_path.read_bytes()
        decrypted = self.decrypt_bytes(enc_data)
        out_path.write_bytes(decrypted)
        return out_path

    @staticmethod
    def sha256_text(text: str) -> str:
        """Computes SHA-256 hex digest of string."""
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    @staticmethod
    def sha256_file(file_path: Union[str, Path]) -> str:
        """Computes SHA-256 hex digest of a file for deliverable verification."""
        path = Path(file_path)
        if not path.exists():
            return ""
        hasher = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()

    @staticmethod
    def generate_manifest(folder_path: Union[str, Path]) -> dict:
        """
        Generates a cryptographic SHA-256 manifest of all files in a folder.
        Proves genuine work authenticity for client milestone approval.
        """
        folder = Path(folder_path)
        manifest = {}
        if not folder.exists():
            return manifest

        for p in folder.rglob("*"):
            if p.is_file() and not p.name.endswith(".sha256") and not p.name.endswith(".enc") and not p.name.endswith(".pyc") and "__pycache__" not in p.parts:
                rel_path = str(p.relative_to(folder)).replace("\\", "/")
                manifest[rel_path] = CryptoVault.sha256_file(p)
        return manifest


# Singleton instance
vault = CryptoVault()

if __name__ == "__main__":
    test_str = "ASMA-OS: Confidential client contract - $500 milestone"
    enc = vault.encrypt_string(test_str)
    dec = vault.decrypt_string(enc)
    assert test_str == dec
    print("CryptoVault AES-256-GCM Verified successfully.")
    print(f"Key Hash: {CryptoVault.sha256_text(vault.key.hex())[:16]}...")
