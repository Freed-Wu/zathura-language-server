if $type == "option" then
  .properties.set.properties
elif $type == "command" or $cursor[1] == 0 then
  .properties
elif $type == "mode_name" then
  .properties.map.properties
elif [$type] | inside(["key", "function", "argument"]) then
  .properties.map.properties.normal.items.properties[$type] | if .enum == null then .anyOf[0] end | .enum | map({(.): null}) | add
else
  {}
end | to_entries[] |
if .key | (if $complete then startswith($text) else . == $text end) then
  {
    label: .key,
    insert_text: .key,
    kind: (
      if $type == "option" then
        $enums.CompletionItemKind.Variable
      elif $type == "command" then
        $enums.CompletionItemKind.Keyword
      else
        $enums.CompletionItemKind.Constant
      end
    ),
    documentation: (
      if $type == "option" or $type == "command" then
        {kind: "markdown", value: .value.description}
      else
        null
      end
    )
  }
else
  empty
end
