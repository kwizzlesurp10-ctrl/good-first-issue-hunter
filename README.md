# GoodFirstIssueHunter - Mythic-level Agent Search Automation

Mythic-tier LLM-orchestrated browser hunter for high-signal "good first issue" GitHub tasks (LangGraph/CrewAI + Supabase ledger ready, full research spec alignment).

## Features
- Core hunter with --dry-run powered by live MCP GitHub search data.
- LangGraph-style multi-agent demo (pure Python state machine for standalone use):
  - SearchAutomation (query gen + live MCP)
  - HuntNode
  - StrategistNode
  - FilterNode
  - MCPEnrichNode (repo health, comments via grok_com_github)
  - MCPCommentDraftNode (safe natural-lang drafts with human_review_required)
  - HumanReviewNode (v5 approval gate)
  - CareerCoPilotNode (v6: weekly plan, portfolio highlights, skills correlation/job market)
  - PortfolioNode (final contribution_plan.json)
- Full pipeline tested with fresh live MCP data from recent good first issues.
- Safe, ethical, human-reviewed commenting via MCP add_issue_comment.
- Designed for extension to real LangGraph, Supabase, etc.

## Usage
python good_first_issue_hunter_langgraph.py --dry-run --user-id keith --tech-stacks Python,TypeScript --require-human-review

# Or load previous ledger
python good_first_issue_hunter_langgraph.py --ledger goodfirstissue_hunter_ledger.json

See launch_good_first_issue_hunter.py for setup instructions and real hunt (browser + Ollama).

## Research
Based on mythic_goodfirstissuehunter_build_20260612. Preserves researchId, QUALITY_JUDGE_PROMPT, ledger contract, etc.

## Evolution
v1: Browser hunter + ledger
v2: LangGraph multi-agent
v3: MCP GitHub integration
v4: Safe commenting
v5: Human-in-the-loop
v6: Career co-pilot
v7: Search automation with live MCP data + query gen
