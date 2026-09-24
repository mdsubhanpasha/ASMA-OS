"""
Project ASMA - Private Income OS
Author: Md Subhan Pasha
Dedicated to: Asma

Unified Command Line Interface (cli.py)
Usage:
  python cli.py status           # Display daily $500 target and PayPal status
  python cli.py scan             # Scan Remote OK, WWR, Gun.io, Toptal for $500+ jobs
  python cli.py jobs             # List ingested high-ticket jobs
  python cli.py demo <job_id>    # Generate 3 genuine demos with SHA-256 manifest
  python cli.py pitch <job_id>   # Draft senior architect proposal with Groq Llama 3.3 70B
  python cli.py deliver <client> # Scaffold workspace, QA checklist, and tests
  python cli.py invoice <client> # Generate $500 invoice PDF and update ledger
"""

import sys
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from job_ingest import scan_all_platforms, list_jobs, get_job_by_id
from demo_factory import generate_demos_for_job_id
from negotiate_agent import negotiate_agent, load_pending_emails
from delivery_agent import delivery_agent
from paypal_daily import (
    get_daily_reflect,
    load_ledger,
    generate_invoice_pdf,
    record_milestone_settlement,
    mark_milestone_paid,
    PAYPAL_RECEIVER,
    PAYPAL_LINK,
    DAILY_TARGET_USD
)


def cmd_status():
    reflect = get_daily_reflect()
    print("=" * 65)
    print("PROJECT ASMA - PRIVATE INCOME OS")
    print("Dedicated to: Asma | Sole Author: Md Subhan Pasha")
    print("=" * 65)
    print(f"Status: {reflect['reflect_string']}")
    print(f"Daily Target: ${int(DAILY_TARGET_USD):,} USD")
    print(f"Earned / Paid Today: ${reflect['today_paid']:,.2f}")
    print(f"Ready for Settlement: ${reflect['today_ready']:,.2f}")
    print(f"PayPal Direct: {PAYPAL_LINK}")
    print("=" * 65)


def cmd_scan():
    print("Scanning Remote OK, We Work Remotely, Gun.io, Toptal...")
    res = scan_all_platforms()
    print(f"Scan complete: {res['qualified_500_plus']} qualified $500+ jobs saved to vault.")


def cmd_jobs():
    jobs = list_jobs()
    print(f"\nIngested High-Ticket Opportunities ({len(jobs)} total):\n")
    for j in jobs[:15]:
        print(f"ID #{j['id']:<3} | [{j['platform']}] {j['title'][:40]:<40} | {j['budget']:<20} | {j['company']}")


def cmd_demo(job_id: int):
    print(f"Generating 3 genuine demos for Job ID {job_id}...")
    res = generate_demos_for_job_id(job_id)
    if not res:
        print(f"Job ID {job_id} not found.")
        return
    print(f"Success! Demos generated in: {res['demo_dir']}")
    for f in res["files"]:
        print(f" - {f}")


def cmd_pitch(job_id: int):
    job = get_job_by_id(job_id)
    if not job:
        print(f"Job ID {job_id} not found.")
        return
    print(f"Drafting proposal for '{job['title']}' ({job['company']}) via Groq Llama 3.3 70B...")
    draft = negotiate_agent.draft_proposal(job)
    print(f"Draft ID: {draft['id']} [Status: {draft['status']}]")
    print(f"Subject: {draft['subject']}")
    print("-" * 60)
    print(draft["body"])


def cmd_deliver(client_name: str, project_title: str = "Enterprise Engineering Milestone"):
    print(f"Scaffolding deliverable repository for '{client_name}'...")
    ws = delivery_agent.create_workspace(client_name, project_title, 500.0)
    print(f"Deliverable workspace created at: {ws['workspace_path']}")
    print(f"SHA-256 manifest: {ws['manifest_file']}")


def cmd_invoice(client_name: str, project_name: str = "Python & Architecture Milestone"):
    print(f"Generating $500 invoice PDF for '{client_name}'...")
    pdf = generate_invoice_pdf(client_name, project_name, 500.0)
    print(f"Invoice PDF generated: {pdf}")
    record_milestone_settlement(client_name, project_name, 500.0, "cli_verified")
    print("Ledger updated in data/asma_ledger.csv.")


def main():
    parser = argparse.ArgumentParser(description="ASMA OS Command Line Interface")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("status", help="Show daily $500 reflect and PayPal status")
    subparsers.add_parser("scan", help="Scan job platforms for $500+ milestones")
    subparsers.add_parser("jobs", help="List ingested jobs")

    demo_p = subparsers.add_parser("demo", help="Generate 3 genuine demos for a job")
    demo_p.add_argument("job_id", type=int, help="Job ID from vault")

    pitch_p = subparsers.add_parser("pitch", help="Draft proposal with Groq Llama 3.3 70B")
    pitch_p.add_argument("job_id", type=int, help="Job ID from vault")

    deliv_p = subparsers.add_parser("deliver", help="Scaffold client workspace")
    deliv_p.add_argument("client", type=str, nargs="?", default="CognitiveOps Corp", help="Client Name (default: CognitiveOps Corp)")
    deliv_p.add_argument("--project", type=str, default="Enterprise Engineering Milestone", help="Project Title")

    inv_p = subparsers.add_parser("invoice", help="Generate $500 invoice PDF")
    inv_p.add_argument("client", type=str, nargs="?", default="CognitiveOps Corp", help="Client Name (default: CognitiveOps Corp)")
    inv_p.add_argument("--project", type=str, default="Production Milestone", help="Project Title")

    args = parser.parse_args()

    if args.command == "status" or not args.command:
        cmd_status()
    elif args.command == "scan":
        cmd_scan()
    elif args.command == "jobs":
        cmd_jobs()
    elif args.command == "demo":
        cmd_demo(args.job_id)
    elif args.command == "pitch":
        cmd_pitch(args.job_id)
    elif args.command == "deliver":
        cmd_deliver(args.client, args.project)
    elif args.command == "invoice":
        cmd_invoice(args.client, args.project)


if __name__ == "__main__":
    main()
