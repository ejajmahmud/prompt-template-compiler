"""Zero-dependency strict prompt template rendering engine."""
import re
from typing import Dict, Any


class PromptCompiler:
    @staticmethod
    def render(template: str, context: Dict[str, Any]) -> str:
        rendered = template

        # Handle simple conditionals: {% if var %}...{% endif %}
        def _cond_replace(match):
            var_name = match.group(1).strip()
            body = match.group(2)
            if context.get(var_name):
                return body
            return ""

        rendered = re.sub(r"\{%\s*if\s+([a-zA-Z0-9_]+)\s*%\}(.*?)\{%\s*endif\s*%\}", _cond_replace, rendered, flags=re.DOTALL)

        # Handle variable replacement: {{ var }}
        def _var_replace(match):
            var_name = match.group(1).strip()
            if var_name not in context:
                raise KeyError(f"Template rendering failed: missing required variable '{var_name}'")
            return str(context[var_name])

        rendered = re.sub(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}", _var_replace, rendered)
        return rendered
