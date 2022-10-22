json := $(wildcard assets/json/*.json)
txt := $(wildcard doc/*.txt)

.PHONY: default
default: all

.PHONY: all
all: test $(json) $(txt)

.PHONY: test
test:
	themis

assets/json/%.json: scripts/%.py
	$< > $@

$(txt): $(wildcard **/*.vim) addon-info.json
	vimdoc .

clean:
	rm -rf $(json) $(txt)
