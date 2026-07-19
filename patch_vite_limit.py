import re

with open('vite.config.ts', 'r') as f:
    content = f.read()

if 'build: {' not in content:
    content = content.replace('server: {', 'build: {\n      chunkSizeWarningLimit: 1000\n    },\n    server: {')

with open('vite.config.ts', 'w') as f:
    f.write(content)
