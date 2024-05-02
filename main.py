from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
from interpret_model import Level

entity_mm = metamodel_from_file('grammar.tx')

metamodel_export(entity_mm, 'grammar.dot')

model = entity_mm.model_from_file("levels\level3.ddr")

level = Level(debug=True)

level.interpret_level(model)

model_export(model, 'level.dot')
