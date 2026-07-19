with open('server.ts', 'r') as f:
    content = f.read()

content = content.replace('frameSrc: ["\'self\'"],\n      }', 'frameSrc: ["\'self\'"],\n        frameAncestors: ["*"],\n      }')
content = content.replace('crossOriginEmbedderPolicy: false,\n  }));', 'crossOriginEmbedderPolicy: false,\n    frameguard: false,\n  }));')

with open('server.ts', 'w') as f:
    f.write(content)
