## 2025-02-06 - Search Experience & Accessibility
**Learning:** Icon-only buttons (like copy/download) need `aria-label` for screen reader users, and `title` for mouse users.
**Action:** Always add `aria-label` and `title` to dynamically generated buttons that rely on icons.
**Learning:** Async search actions should disable the trigger button and show a loading spinner to prevent double-submissions and provide feedback.
**Action:** Implement loading states (disable + spinner) for all async actions.
**Learning:** HTML attribute values (like `aria-label`) must escape double quotes if they contain user content.
**Action:** Use `.replace(/"/g, '&quot;')` or similar escaping when injecting strings into HTML attributes.
**Learning:** Use `innerHTML` instead of `innerText` when restoring button state if the button might contain HTML elements (icons).
**Action:** Prefer `innerHTML` for state restoration of complex elements.
