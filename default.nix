{
  pkgs ? import <nixpkgs> { },
}:
let
  python = pkgs.python314;
in
python.pkgs.buildPythonApplication rec {

  pname = "meshbot";
  version = "0.0.0";
  pyproject = true;
  src = ./.;

  # run-time dependencies
  propagatedBuildInputs = [
    python.pkgs.meshtastic
  ];

  # test dependencies
  nativeCheckInputs = [
    python.pkgs.mypy
    python.pkgs.black
    python.pkgs.pytest
  ];

  preBuild = ''
    cat > pyproject.toml << EOF
    [project]
    name = "${pname}"
    version = "0.0.0"
    requires-python = "==3.14"
    dependencies = [
      "meshtastic==2.7.7",
    ]
    [project.scripts]
    meshbot = "main:main"
    EOF
  '';

  checkPhase = ''
    mypy --ignore-missing-imports src
    black --check --diff src
    pytest tests/
  '';
}
