SOURCES_DIR := SOURCES
SPECS_DIR := SPECS

RPM_SPEC_FILE := $(SPECS_DIR)/opentelemetry-collector-rhde-config.spec
RPM_TARGET := rpm

SOURCE_FILES := config.yaml

$(RPM_TARGET): $(addprefix $(SOURCES_DIR)/,$(SOURCE_FILES))
	rpmbuild -ba $(RPM_SPEC_FILE)

$(SOURCES_DIR)/%.yaml: %.yaml
	cp $< $@

copr: $(addprefix $(SOURCES_DIR)/,$(SOURCE_FILES))
	rpmbuild -bs $(RPM_SPEC_FILE)
	copr-cli build miyunari/opentelemetry-collector-rhde-config SRPMS/opentelemetry-collector-rhde-config-1.0-1.fc39.src.rpm

