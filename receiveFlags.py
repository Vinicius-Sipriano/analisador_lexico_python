from pathlib import Path

def flags(argv):
	if len(argv) < 2:
		# Use default example file if no argument provided
		source_path = Path("examples/example.txt")
	else:
		source_path = Path(argv[1])

	try:
		return source_path.read_text(encoding="utf-8")
	except FileNotFoundError as exc:
		raise SystemExit(f"Arquivo nao encontrado: {source_path}") from exc