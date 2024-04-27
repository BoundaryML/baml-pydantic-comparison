# baml-pydantic-comparison

How to run tests (if using infisical for env vars)

# Note:
This test uses the old `.baml` syntax for building functions (uses `impl`, and oesn't support Jinja templating to write prompts). The new syntax is described in [promptfiddle.com](https://promptfiddle.com).
We will eventually migrate this to the new syntax. Both syntaxes use type-definitions to describe schemas.

## LLama2 test (BAML vs Pydantic/Instructor)

`infisical run --env=dev -- pytest . -k "order_info3" -s --log-cli-level=DEBUG`
