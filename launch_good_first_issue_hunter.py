#!/usr/bin/env python3
"""
Launcher / Setup Helper for GoodFirstIssueHunter (Automation Builder)

This is the recommended entry point for running the mythic-tier hunter
and its LangGraph-style multi-agent continuation demo.

It prints clear setup instructions (Chrome CDP + Ollama + optional deps),
then offers to run the verified --dry-run paths or the LangGraph demo.

Usage:
    python scripts/launch_good_first_issue_hunter.py

It will:
- Check basic Python / requests availability.
- Print the exact commands for real vs dry-run.
- Run the LangGraph demo in --dry-run mode by default (no browser/LLM needed).
- Remind you of the exhaustive memory record in ~/.grok/memory/MEMORY.md
  (use /memory or cat it to recall full session context, researchId, etc.).

Real hunt prerequisites (for when you want live browser control):
1. Start persistent Chrome with remote debugging (your real GitHub login):
   google-chrome-stable --remote-debugging-port=9222 --user-data-dir=~/.grok-browser-profile
   (Log into GitHub once in that profile.)

2. Have Ollama (or compatible) running with a capable model:
   ollama run llama3.1   # or gpt-4o, llava for vision, etc.

3. (Optional for full power) pip install playwright && playwright install chromium

Then run:
    python examples/good_first_issue_hunter_agent.py \
        --user-id keith \
        --tech-stacks Python,TypeScript \
        --min-repo-stars 500 \
        --max-issues 8 \
        --freshness-days 60

For the multi-agent LangGraph demo (always works):
    python examples/good_first_issue_hunter_langgraph.py --dry-run --user-id keith

The output contribution_plan.json includes a "memory_note_ready" section
you can feed directly to Grok Build's /remember for long-term recall.

See the hunter docstring and examples/ for full evolution (v1 browser hunter + v2 langgraph layer).
The researchId "mythic_goodfirstissuehunter_build_20260612" is preserved everywhere.

ForgeAI note: This launcher is documentation + convenience only (no core logic change).
"""

import os
import subprocess
import sys

def main():
    print("=" * 70)
    print("GOOD FIRST ISSUE HUNTER — LAUNCHER / SETUP HELPER")
    print("Mythic-tier build continuation (v1 + v2 LangGraph demo)")
    print("researchId: mythic_goodfirstissuehunter_build_20260612")
    print("=" * 70)

    print("\n[1/3] Environment check (this env is intentionally minimal for demos):")
    try:
        import requests
        print("  requests: OK")
    except Exception as e:
        print(f"  requests: MISSING ({e})")

    print("\n[2/3] Recommended setup for REAL hunts (browser + LLM):")
    print("  1. Chrome with CDP (run once, keep open):")
    print("     google-chrome-stable --remote-debugging-port=9222 \\")
    print("       --user-data-dir=~/.grok-browser-profile")
    print("     (Log into GitHub in that profile.)")
    print("  2. Ollama + model:")
    print("     ollama run llama3.1")
    print("  3. (Optional for full features) pip install playwright && playwright install chromium")
    print("  4. Run a live hunt (example):")
    print("     python examples/good_first_issue_hunter_agent.py \\")
    print("       --user-id keith \\")
    print("       --tech-stacks Python,TypeScript,Next.js \\")
    print("       --min-repo-stars 500 --max-issues 8 --freshness-days 60")

    print("\n[3/3] Verified demo paths (work with zero extra deps):")
    print("  - Main hunter dry-run (ledger + table):")
    print("    python examples/good_first_issue_hunter_agent.py --dry-run --user-id keith --tech-stacks Python,TypeScript")
    print("  - LangGraph multi-agent search automation demo (SearchAutomation -> Hunt -> ... -> MCPEnrich -> MCPCommentDraft -> HumanReview(v5) -> CareerCoPilot(v6) -> Portfolio):")
    print("    python examples/good_first_issue_hunter_langgraph.py --dry-run --user-id keith --tech-stacks Python,TypeScript")
    print("    # With human-in-the-loop gate:")
    print("    python examples/good_first_issue_hunter_langgraph.py --dry-run --user-id keith --tech-stacks Python,TypeScript --require-human-review")

    print("\nMemory record location (exhaustive session brain dump):")
    print("  ~/.grok/memory/MEMORY.md  (cat it or use /memory in Grok Build)")
    print("  Contains full crash-recovery story, all tool calls, code states, decisions, and this launcher.")

    print("\nOutput artifacts will appear in this dir (ledgers, contribution_plan.json).")
    print("They are designed for LangGraph checkpoints, Supabase, Memory Garden, or /remember.")

    print("\n" + "=" * 70)
    print("Running the LangGraph demo now for convenience (dry-run mode)...")
    print("=" * 70)

    # Run the verified demo
    try:
        result = subprocess.run(
            [sys.executable, "examples/good_first_issue_hunter_langgraph.py", "--dry-run", "--user-id", "keith"],
            cwd=os.path.dirname(os.path.dirname(__file__)),  # project root
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("Demo run failed (unexpected in this env):", e)
        print(e.stdout)
        print(e.stderr)

    print("\nLauncher complete. See contribution_plan.json (or re-run the commands above).")
    print("To proceed further (MCP GitHub follow-up, real browser hunt, full LangGraph port): provide next instruction.")

if __name__ == "__main__":
    main()
