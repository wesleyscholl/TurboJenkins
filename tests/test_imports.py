def test_imports():
    import importlib
    importlib.import_module("turbojenkins.cli")
    importlib.import_module("turbojenkins.jenkins_client")
    importlib.import_module("turbojenkins.ai_engine")
