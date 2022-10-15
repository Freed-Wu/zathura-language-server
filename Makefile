.PHONY: default
default: all

.PHONY: all
all: $(wildcard assets/json/*.json)

assets/json/%.json: scripts/%.py
	$< > $@

clean:
	rm -rf assets/json/*.json
