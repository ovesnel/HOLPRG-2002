.DEFAULT_GOAL := help
SPHINXOPTS    ?= -W
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build
DOCKER_COMPOSE_FILES = -f docker-compose.yml
BACKUP_NAME = backup-production-latest.tar.gz

.PHONY: help
help:	## Show this help
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: test-local-docs
test-local-docs:
	docker run -it --rm -v `PWD`:/repo containers.cisco.com/aide/sphinx-tools validate.sh

.PHONY: show-local-docs
show-local-docs:
	docker run -it --rm -p 8000:8000 -v `PWD`:/repo containers.cisco.com/aide/sphinx-tools cicd.sh
