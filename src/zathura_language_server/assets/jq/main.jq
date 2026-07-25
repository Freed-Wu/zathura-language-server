(if $cursor[1] == 0 then "command" else $nodes[0].type end) as $type |
if $type == "option" then
  .properties.set.properties
elif $type == "command" then
  .properties
elif $type == "mode_name" then
  .properties.map.properties
elif [$type] | inside(["key", "function", "argument"]) then
  .properties.map.properties.normal.items.properties[$type] | if .enum == null then .anyOf[0] end | .enum | map({(.): null}) | add
else
  {}
end | to_entries[] |
if .key | ($nodes[0].text as $text | if $complete then startswith($text) else . == $text end) then
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
      if .value.description then
        {kind: "markdown", value: .value.description}
      else
        null
      end
    )
  }
else
  empty
end
