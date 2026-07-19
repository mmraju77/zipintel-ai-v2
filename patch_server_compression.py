import re

with open('server.ts', 'r') as f:
    content = f.read()

content = content.replace(
    'import helmet from "helmet";',
    'import helmet from "helmet";\nimport compression from "compression";'
)

content = content.replace(
    'app.use(helmet(',
    'app.use(compression());\n  app.use(helmet('
)

with open('server.ts', 'w') as f:
    f.write(content)
