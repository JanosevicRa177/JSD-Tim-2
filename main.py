from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export

entity_mm = metamodel_from_file('grammar.tx')

metamodel_export(entity_mm, 'grammar.dot')