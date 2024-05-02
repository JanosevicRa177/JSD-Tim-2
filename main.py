from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

entity_mm = metamodel_from_file('grammar.tx')

metamodel_export(entity_mm, 'grammar.dot')

model = entity_mm.model_from_file("levels\level2.ddr")

model_export(model, 'level.dot')
