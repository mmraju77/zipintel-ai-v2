import re

with open('src/components/InfrastructureInsights.tsx', 'r') as f:
    content = f.read()

# Replace main container with exactly what was asked
content = content.replace(
    'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-8 w-full"',
    'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-8 w-full"'
)

with open('src/components/InfrastructureInsights.tsx', 'w') as f:
    f.write(content)

with open('src/pages/CountryPage.tsx', 'r') as f:
    content2 = f.read()

# Make the infrastructure insights take full width so it doesn't get squished
content2 = content2.replace(
    '<div className="md:col-span-1">\n          <InfrastructureInsights',
    '</div>\n      <div className="max-w-5xl mx-auto mt-6">\n        <div className="w-full">\n          <InfrastructureInsights'
)
content2 = content2.replace(
    '<div className="mt-6">\n            <MonetizationNodes zone="sidebar" />\n          </div>\n        </div>',
    '</div>\n      </div>\n      <div className="max-w-5xl mx-auto grid md:grid-cols-3 gap-6 mt-6">\n        <div className="md:col-span-3">\n          <div className="mt-6">\n            <MonetizationNodes zone="sidebar" />\n          </div>\n        </div>'
)

with open('src/pages/CountryPage.tsx', 'w') as f:
    f.write(content2)

