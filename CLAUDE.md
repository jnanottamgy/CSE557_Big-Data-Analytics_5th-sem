# Repository rules

## Commit identity (mandatory)

Every commit pushed to this repository must be authored and committed as **jnanottamgy**:

- `user.name`:  `jnanottamgy`
- `user.email`: `192404215+jnanottamgy@users.noreply.github.com` (GitHub noreply address, links commits to the account)

Before committing, make sure the repo-local git config is set:

```sh
git config user.name "jnanottamgy"
git config user.email "192404215+jnanottamgy@users.noreply.github.com"
```

A SessionStart hook in `.claude/settings.json` applies this automatically.

- Do not add a `Co-Authored-By: Claude ...` trailer to commit messages.
- Never commit or push under any other name or email.
