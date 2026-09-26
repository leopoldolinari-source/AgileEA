"""Definiciones del glosario de AgileEA. Genera estratos/sql/glosario.sql.

Uso: python3 tools/glosario.py
Categoría = nombre de la columna (o concepto); valor '' = definición del concepto.
"""
G = {
 'lifecycle': ('Ciclo de vida', 'Fase en la que está la aplicación dentro de su vida útil, desde que se planifica hasta que se retira. Con fechas por fase se arma el roadmap.', [
  ('Plan', None, 'Aplicación planificada o aprobada, todavía no incorporada al uso operativo.'),
  ('Phase In', None, 'Aplicación en implementación, transición o despliegue progresivo hacia el uso operativo.'),
  ('Active', None, 'Aplicación actualmente activa y en uso dentro del portfolio.'),
  ('Phase Out', None, 'Aplicación en proceso de retiro, reemplazo o reducción progresiva de uso.'),
  ('End of Life', None, 'Aplicación retirada o fuera de su ciclo de vida objetivo; no debería recibir nuevas inversiones funcionales salvo excepciones.')]),
 'business_criticality': ('Criticidad de negocio', 'Impacto que tendría para el negocio la indisponibilidad de la aplicación o capacidad.', [
  ('Administrative Service', None, 'Soporta tareas administrativas, con bajo impacto en las operaciones del negocio.'),
  ('Business Operational', None, 'Importante para las operaciones del día a día, pero no impacta críticamente los objetivos estratégicos.'),
  ('Business Critical', None, 'Vital para las operaciones y soporta directamente objetivos estratégicos. Una indisponibilidad prolongada impactaría significativamente a la organización.'),
  ('Mission Critical', None, 'Esencial para la misión core y los objetivos estratégicos. Incluso una breve indisponibilidad puede tener consecuencias severas.')]),
 'functional_fit': ('Ajuste funcional', 'Qué tan bien cubre la aplicación las necesidades funcionales del negocio (1 = peor, 4 = mejor).', [
  ('1', '1 - Unreasonable', 'No cubre adecuadamente las necesidades funcionales actuales del negocio.'),
  ('2', '2 - Insufficient', 'Presenta gaps funcionales importantes y requiere complementos o trabajo manual.'),
  ('3', '3 - Appropriate', 'Cubre adecuadamente las necesidades actuales, con limitaciones menores.'),
  ('4', '4 - Perfect', 'Cubre de forma integral las necesidades actuales y acompaña la evolución esperada.')]),
 'technical_fit': ('Ajuste técnico', 'Qué tan adecuada es la tecnología de la aplicación en estándares, operación, riesgo y arquitectura (1 = peor, 4 = mejor).', [
  ('1', '1 - Inappropriate', 'No cumple criterios técnicos, operativos o de riesgo aceptables.'),
  ('2', '2 - Unreasonable', 'Tiene limitaciones técnicas relevantes, deuda o riesgos que condicionan su sostenibilidad.'),
  ('3', '3 - Adequate', 'Cumple adecuadamente las necesidades técnicas actuales, aunque no está totalmente alineada con el objetivo futuro.'),
  ('4', '4 - Fully Appropriate', 'Está plenamente alineada con estándares técnicos, operación, riesgo y arquitectura objetivo.')]),
 'clasificacion': ('Clasificación', 'Rol de la capacidad en la estrategia del negocio.', [
  ('Estratégica', None, 'Función orientada al mercado que permite diferenciarse de los competidores. Posee alta varianza competitiva: con los mismos insumos, distintas organizaciones obtienen resultados distintos. Es el objeto prioritario de la inversión en transformación digital.'),
  ('Operativa', None, 'Actividad técnica obligatoria e indispensable para la existencia y viabilidad del negocio. Opera en flujos específicos y secuenciales con alcance delimitado, y su interrupción compromete la continuidad. Suele estar estandarizada, con baja varianza entre operadores maduros.'),
  ('Transversal', None, 'Sostiene el funcionamiento de la organización y el cumplimiento regulatorio. No pertenece a ningún dominio y aplica a todos. No genera valor comercial externo de forma directa, pero su degradación produce riesgos sistémicos.')]),
 'cadena_de_valor': ('Cadena de valor', 'Etapa de la cadena de valor upstream en la que opera la capacidad.', [
  ('Exploración & Evaluación de Activos', None, 'Localizar yacimientos de crudo y gas natural bajo la superficie terrestre y ejecutar perforaciones iniciales para validar si el hallazgo es comercialmente explotable.'),
  ('Planificación del Desarrollo de Activos', None, 'Una vez que el activo se declara viable, se diseñan las estrategias de explotación, la ingeniería de las instalaciones de superficie y el programa definitivo de perforación.'),
  ('Desarrollo de Activos', None, 'Construcción física de la infraestructura industrial y perforación en masa de los pozos productores planificados.'),
  ('Producción & Transporte', None, 'Extracción continua del hidrocarburo, su separación primaria en campo, el almacenamiento temporal y el despacho seguro hacia los sistemas de refinación o exportación.')]),
 'pace_layering': ('Pace layering', 'Ritmo de cambio esperado de la capacidad (modelo de Gartner).', [
  ('Commodity', None, 'Ritmo de cambio lento y estable. 70% del portafolio. Ciclo de 2 a 7 años.'),
  ('Differentiation', None, 'Ritmo de cambio moderado. 20% del portafolio. Ciclo de 1 a 2 años.'),
  ('Innovation', None, 'Ritmo de cambio rápido y experimental. 5 a 10% del portafolio. Ciclo de 2 a 6 meses.')]),
 'regulatory_impact': ('Impacto regulatorio', 'Grado en que la capacidad está sujeta a regulación y controles externos.', [
  ('Low', None, 'Impacto regulatorio bajo o indirecto; mayormente gobernanza interna.'),
  ('Medium', None, 'Existe cumplimiento relevante (contrataciones, documentación, controles) pero con menor frecuencia, mayor tolerancia de tiempo o impacto más indirecto.'),
  ('High', None, 'La capacidad está directamente regulada y requiere permisos, estudios o reportes obligatorios frecuentes, auditorías, y presenta riesgo de sanciones por no conformidad ambiental, de seguridad, integridad o medición.')]),
 'tipo_aplicacion': ('Tipo de aplicación', 'Origen de la aplicación.', [
  ('Comercial', None, 'Aplicación adquirida a un proveedor externo y utilizada bajo un modelo comercial de licenciamiento, suscripción o mantenimiento.'),
  ('Desarrollo', None, 'Aplicación desarrollada específicamente para la organización, de forma interna o a medida, para cubrir necesidades propias del negocio.'),
  ('Open Source', None, 'Aplicación distribuida bajo una licencia de código abierto, que permite usar, estudiar, modificar y redistribuir el software según sus términos.')]),
 'deployment': ('Despliegue', 'Dónde corre y quién opera la aplicación.', [
  ('On-Premise', None, 'Aplicación desplegada y operada sobre infraestructura administrada por la organización.'),
  ('SaaS', None, 'Aplicación consumida como servicio y operada principalmente por el proveedor, normalmente mediante una suscripción.'),
  ('Private Cloud', None, 'Aplicación desplegada sobre infraestructura cloud dedicada o aislada para la organización.'),
  ('Public Cloud', None, 'Aplicación desplegada sobre infraestructura de nube pública provista y operada por un tercero.'),
  ('Hybrid', None, 'Aplicación cuya arquitectura combina componentes On-Premise y/o nubes privadas y públicas.'),
  ('Hosted', None, 'Aplicación alojada en infraestructura de un tercero dedicada o administrada externamente, sin implicar necesariamente un modelo SaaS.')]),
 'modelo_comercial': ('Modelo comercial', 'Forma en que se adquiere el derecho de uso del software.', [
  ('Perpetual', None, 'Licencia comprada una vez con derecho de uso indefinido; normalmente se suma soporte y mantenimiento anual.'),
  ('Subscription', None, 'Derecho de uso por un período; al vencer, se renueva o se pierde el acceso.'),
  ('Usage Based', None, 'Se paga según el consumo medido (horas, transacciones, volumen de datos).'),
  ('Enterprise Agreement', None, 'Acuerdo corporativo que cubre un conjunto amplio de productos o usuarios por un período, con condiciones negociadas.'),
  ('Sin costo', None, 'Uso sin cargo: open source, incluido en otro contrato o sin cargo del proveedor.')]),
 'metrica_licencia': ('Métrica de licencia', 'Unidad con la que se cuenta la licencia.', [
  ('Named User', None, 'Asignada a una persona específica; solo esa persona puede usarla.'),
  ('Concurrent / Floating', None, 'Pool compartido: limita cuántas personas la usan al mismo tiempo, no quiénes.'),
  ('CPU / Core', None, 'Se licencia por procesadores o núcleos del servidor donde corre.'),
  ('Server / Instance', None, 'Se licencia por servidor o instancia instalada.'),
  ('Site', None, 'Uso ilimitado dentro de una ubicación física definida.'),
  ('Enterprise', None, 'Uso ilimitado en toda la organización.'),
  ('Usage', None, 'Se mide y paga por consumo.')]),
 'tipo_gasto': ('Tipo de gasto', 'Naturaleza contable del gasto.', [
  ('CAPEX', None, 'Inversión de capital: compra de activos o licencias perpetuas que se amortizan en varios años.'),
  ('OPEX', None, 'Gasto operativo recurrente del período: suscripciones, soporte y mantenimiento, servicios.')]),
 'time': ('Matriz TIME', 'Clasificación del portafolio de aplicaciones según ajuste funcional y técnico (Gartner / LeanIX).', [
  ('Tolerar', None, 'Buen ajuste técnico pero bajo ajuste funcional: se mantiene sin invertir en funcionalidad, minimizando su costo.'),
  ('Invertir', None, 'Alto ajuste funcional y técnico: aplicación en la que conviene seguir invirtiendo.'),
  ('Migrar', None, 'Alto ajuste funcional pero bajo ajuste técnico: aporta valor, pero su tecnología es un riesgo; conviene migrarla a una plataforma adecuada.'),
  ('Eliminar', None, 'Bajo ajuste funcional y técnico: candidata a retiro o consolidación.')]),
 'rol_aplicacion': ('Rol en la aplicación', 'Responsabilidad de una persona sobre la aplicación.', [
  ('Application Business Owner', None, 'Responsable de negocio: define prioridades, aprueba cambios y responde por el valor que entrega la aplicación.'),
  ('Application Technology Owner', None, 'Responsable técnico: arquitectura, operación, seguridad y ciclo de vida tecnológico de la aplicación.'),
  ('Product Owner', None, 'Gestiona la evolución funcional y el backlog; es el nexo entre los usuarios y el equipo técnico.'),
  ('Key User', None, 'Usuario referente: conoce el uso en profundidad, valida cambios y capacita a otros usuarios.')]),
 'rol_proveedor': ('Rol del contacto', 'Para qué se contacta a la persona del proveedor.', [
  ('Comercial', None, 'Cotizaciones, renovaciones y condiciones comerciales.'),
  ('Soporte técnico', None, 'Incidentes, consultas técnicas y mesa de ayuda del producto.'),
  ('Licenciamiento', None, 'Altas, bajas y cantidades de licencias, claves y servidores de licencias.'),
  ('Otro', None, 'Otro tipo de contacto.')]),
 'habilita_imputacion': ('Pagador', 'La organización puede recibir imputación de costos: aparece como pagadora en contratos y costos.', []),
 'madurez': ('Madurez', 'Nivel de madurez de una capacidad en cinco dimensiones: procesos, tecnología, datos, organización y desempeño (1 a 5).', [
  ('1', '1 - Initial / Ad Hoc', 'Informal y dependiente de personas.'),
  ('2', '2 - Managed / Repeatable', 'Repetible, con prácticas reconocibles pero poco formalizadas.'),
  ('3', '3 - Defined / Standardized', 'Definido y estandarizado, con roles y reglas claras.'),
  ('4', '4 - Measured / Quantitatively Managed', 'Medido y gestionado con indicadores.'),
  ('5', '5 - Optimizing / Leading AI', 'Optimización continua, con modelos predictivos e IA.')]),
 'brecha': ('Brecha de madurez', 'Distancia entre la madurez objetivo y el promedio actual de las cinco dimensiones. Cerrarla implica llevar cada dimensión al nivel objetivo. El objetivo se carga por subcapacidad N3 (madurez_objetivo).', []),
}
NIV = {
 'process': ('Madurez · Procesos', ['Informal y no documentado. Cada persona lo resuelve a su manera.', 'Secuencia habitual reconocible, sin documentación punta a punta.', 'Documentado, con roles, entregables y tiempos definidos.', 'Gestionado por indicadores, con ciclo de revisión y ajuste.', 'Se optimiza de forma continua a partir de la evidencia que genera.']),
 'technology': ('Madurez · Tecnología', ['Herramientas de escritorio de uso individual, sin integración.', 'Herramientas específicas de la disciplina, con carga y traspaso manual.', 'Plataforma estándar de la disciplina, con integración parcial al ecosistema.', 'Integración entre plataformas, con datos disponibles en tiempo real o cercano.', 'Automatización avanzada, con modelos predictivos incorporados al flujo.']),
 'data': ('Madurez · Datos', ['Dato disperso, sin dueño ni criterio de calidad. Se reconstruye cada vez.', 'Dato con ubicación conocida y formato acordado, sin control de versiones.', 'Estándares y dueño definidos, con reglas básicas de calidad y trazabilidad.', 'Dato certificado, versionado y disponible para consumo automatizado.', 'Dato como activo gobernado, base de modelos predictivos y de asistentes.']),
 'organization': ('Madurez · Organización', ['Sin rol definido. Depende del conocimiento de una persona.', 'Responsable identificable, sin rol formalizado ni respaldo.', 'Roles formales y foros de decisión establecidos.', 'Gobernanza activa entre áreas, con escalamiento definido.', 'Cultura de mejora continua, con contraste sistemático contra la industria.']),
 'performance': ('Madurez · Desempeño', ['No se mide. El resultado se conoce cuando falla.', 'Se registran resultados, sin indicador ni comparación sistemática.', 'Indicadores definidos y reportados, sin análisis periódico del desvío.', 'Desempeño medido, analizado periódicamente y realimentado a la decisión.', 'Desempeño anticipado por modelos, no solo medido a posteriori.']),
}
LBL = ['1 - Initial / Ad Hoc', '2 - Managed / Repeatable', '3 - Defined / Standardized', '4 - Measured / Quantitatively Managed', '5 - Optimizing / Leading AI']
for dim, (name, descs) in NIV.items():
    G['nivel_' + dim] = (name, f'{name.split(" · ")[1]}: nivel de 1 a 5.', [(str(i + 1), LBL[i], d) for i, d in enumerate(descs)])

def rows():
    for cat, (label, concept, items) in G.items():
        yield cat, '', label, concept, 0
        for i, (val, et, desc) in enumerate(items, 1):
            yield cat, val, et, desc, i

def sql():
    q = lambda s: 'NULL' if s is None else "'" + s.replace("\\", "\\\\").replace("'", "''") + "'"
    out = ["-- Glosario de AgileEA: definiciones que se muestran como tooltips.",
           "-- Categoría = columna o concepto; valor '' = definición del concepto.",
           "CREATE TABLE IF NOT EXISTS `glosario` (",
           "  `id_glosario` int(11) NOT NULL AUTO_INCREMENT,",
           "  `categoria` varchar(60) NOT NULL,",
           "  `valor` varchar(120) NOT NULL DEFAULT '',",
           "  `etiqueta` varchar(160) DEFAULT NULL,",
           "  `descripcion` text NOT NULL,",
           "  `orden` smallint(6) NOT NULL DEFAULT 0,",
           "  PRIMARY KEY (`id_glosario`),",
           "  UNIQUE KEY `uk_glosario` (`categoria`, `valor`)",
           ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;", "",
           "-- Carga inicial. Si ya existe, actualiza el texto (no borra lo que hayas agregado).",
           "INSERT INTO `glosario` (`categoria`, `valor`, `etiqueta`, `descripcion`, `orden`) VALUES"]
    out.append(",\n".join(f"({q(c)}, {q(v)}, {q(e)}, {q(d)}, {o})" for c, v, e, d, o in rows()))
    out[-1] += "\nON DUPLICATE KEY UPDATE `etiqueta` = VALUES(`etiqueta`), `descripcion` = VALUES(`descripcion`), `orden` = VALUES(`orden`);"
    return "\n".join(out) + "\n"

if __name__ == '__main__':
    import json, os, sys
    base = os.path.join(os.path.dirname(__file__), '..', 'estratos')
    open(os.path.join(base, 'sql', 'glosario.sql'), 'w', encoding='utf-8').write(sql())
    # Para la demo sin base: agrega el glosario a data.json si existe
    dj = os.path.join(base, 'data.json')
    if os.path.exists(dj):
        d = json.load(open(dj, encoding='utf-8'))
        d['glosario'] = [dict(categoria=c, valor=v, etiqueta=e, descripcion=ds, orden=o) for c, v, e, ds, o in rows()]
        json.dump(d, open(dj, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(sum(1 for _ in rows()), 'filas')
