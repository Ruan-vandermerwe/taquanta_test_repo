# Python Scripts on GitHub Actions (No Server)

This runs your Python scripts **directly on GitHub Actions** for dev/prod.

## Environments
- Create `dev` and `prod` environments in GitHub.
- Add required reviewers to `prod` to gate production runs.
- Add secrets like `API_KEY`, `SNOWFLAKE_*` in each environment (values can differ).

## Triggers
- Push to `develop` → runs in `dev`
- Push to `main` → runs in `prod` (needs environment approval if configured)
- Manual `workflow_dispatch` with env selection
- Nightly cron

## Entry point
Edit `src/main.py`. The workflow calls `python -m src.main --env $APP_ENV --run-id $GITHUB_RUN_ID`.
