from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,
    root_path='./dynaconf_test/',
    envvar_prefix="DYNACONF",
    settings_files=[
        'settings.toml',
        '.secrets.toml',
        '/vault/secrets/secrets.toml'
    ],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
