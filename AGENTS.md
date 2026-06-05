# Repository Notes

- Keep user-level non-secret chezmoi variables in `.chezmoidata/user.yml`, nested under `user`.
- Keep secrets in `.chezmoidata/secrets.yml`.
- Service configuration should use unified keys under `user.services.<service>.*`.
- Keep shared color variables under `user.colors`.
- Use `user.colors.terminal` for terminal palettes.
- Use `user.colors.theme.usage` for semantic non-terminal color slots and `user.colors.theme.named` for reusable named colors.
- Reuse one color variable across programs when the value matches instead of creating program-specific color fields.
- For locale values: if the value is `en_US` (or `en_US.UTF-8`), keep it as a static string; otherwise templatize it using `{{ .user.locale }}`.
