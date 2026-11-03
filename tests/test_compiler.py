"""Unit tests for PromptCompiler."""
import unittest
from prompt_template_compiler.compiler import PromptCompiler

class TestPromptCompiler(unittest.TestCase):
    def test_variable_interpolation(self):
        tmpl = "Hello {{name}}!"
        res = PromptCompiler.render(tmpl, {"name": "World"})
        self.assertEqual(res, "Hello World!")

    def test_missing_variable_error(self):
        tmpl = "Missing {{key}}"
        with self.assertRaises(KeyError):
            PromptCompiler.render(tmpl, {})

    def test_conditional_block(self):
        tmpl = "{% if show %}Visible{% endif %}"
        self.assertEqual(PromptCompiler.render(tmpl, {"show": True}), "Visible")
        self.assertEqual(PromptCompiler.render(tmpl, {"show": False}), "")

if __name__ == "__main__":
    unittest.main()
