import pydoc
import polyfempy
import re
import queue
import tempfile

packages = queue.Queue()
packages.put("polyfempy")

docs = ""



while not packages.empty():
	package = packages.get()

	with tempfile.NamedTemporaryFile(suffix=".md") as tmp_file:
		with open(tmp_file.name, "w") as f:
			pydoc.doc(package,output=f)

		with open(tmp_file.name, "r") as f:
			lines = f.read()

	if "PACKAGE CONTENTS" in lines:
		process = False

		for line in iter(lines.splitlines()):
			line = line.strip()

			if "PACKAGE CONTENTS" in line:
				process = True
				continue

			if "FILE" in line:
				break

			if not process:
				continue
			if len(line) <= 0:
				continue

			packages.put(package + "." + line)

		continue
	if "CLASSES" in lines:
		process = False


		for line in iter(lines.splitlines()):
			line = line.strip()

			if "CLASSES" in line:
				process = True
				continue

			if "FILE" in line:
				break

			if not process:
				continue
			if len(line) <= 0:
				continue

			if "class " in line:
				break
			if "builtins.object" in line:
				continue

			packages.put(package + "." + line)

		continue

	lines = lines.replace("pybind11_builtins.pybind11_object", "")
	lines = lines.replace("builtins.object", "")
	lines = lines.replace("|", "")
	lines = lines.replace("class ", "## class ")
	lines = lines.replace("self: polyfempy.polyfempy.Solver, ", "")
	lines = lines.replace("self: polyfempy.polyfempy.Solver", "")
	lines = lines.replace("self, ", "")
	lines = lines.replace("self", "")
	lines = lines.replace(" -> None", "")
	lines = lines.replace("[float64[m, n]]", "")
	lines = lines.replace("[int32[m, n]]", "")
	lines = lines.replace("numpy.ndarray", "array")

	tmp = ""

	skipping = False
	next_mark = False
	skip_next = False

	for line in iter(lines.splitlines()):
		line = line.strip()

		if skip_next:
			skip_next = False
			continue
		if len(line) <= 0:
			continue

		if "Python Library Documentation" in line:
			continue

		if "Methods inherited" in line:
			continue

		if "Overloaded function." in line:
			continue

		if "Method resolution order" in line:
			skipping = True

		if "Methods defined here" in line:
			skipping = False
			continue

		if "Data and other attributes defi" in line:
			continue

		if "Data descriptors defined" in line:
			continue

		if "-----------------------------" in line:
			continue

		if "__init__" not in line and re.match(r"__\w+", line):
			skip_next = True
			continue
		if "params()" in line or "get_pde(pde)" in line or "get_problem(problem)" in line or "get_problem()" in line or "name()" in line or "__init__()" in line or "__init__(/, *args, **kwargs)" in line:
			skip_next = True
			continue

		if skipping:
			continue

		if re.match(r'\w+\(\.\.\.\)', line):
			next_mark = True
			continue

		if "class" in line:
			line = line.replace("()", "")

		if re.match(r"\d\. .+", line):
			line = re.sub(r"\d\. ", "", line)
			line.strip()
			next_mark = True

		if next_mark or re.match(r'\w+\(.*\)', line):
			next_mark = False
			xxx = line
			if "__init__" in line:
				line = line.replace("__init__", "init")
			line = "### " + line[0:line.find('(')] +"\n"
			line += "`" + xxx + "`"

		if "## class " in line:
			line = line.replace(package + " = ", "")

		tmp += line + "\n\n"

	docs += tmp + "\n\n\n"
	# break

with open("polyfempy_doc.md", "w") as f:
	f.write(docs)
