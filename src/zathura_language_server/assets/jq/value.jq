if $type == "string" then
  .properties.set.properties[$prev]
else
  empty
end |
if .type == "boolean" then
  "true", "false"
elif .enum != null then
  .enum[]
else
  empty
end |
if (if $complete then startswith($text) else . == $text end) | not then
  empty
end |
{
  label: .,
  insert_text: .,
  kind: $enums.CompletionItemKind.Constant,
}
