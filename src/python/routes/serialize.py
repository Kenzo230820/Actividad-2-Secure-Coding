# src/python/routes/serialize.py
# PASO 4: Insecure Deserialization — usar JSON con schema validado en lugar de pickle
# CODIGO SEGURO
// VULNERABLE — node-serialize permite funciones en el JSON serializado
const serialize = require('node-serialize');

app.post('/restore', (req, res) => {
    const obj = serialize.unserialize(req.body.data);  // ejecuta funciones
    res.json(obj);
});
{"rce":"_$$ND_FUNC$$_function(){require('child_process').exec('id',function(e,o){console.log(o)});}()"}
// SEGURO — JSON.parse con validacion de esquema
const Joi = require('joi');
const schema = Joi.object({ theme: Joi.string(), lang: Joi.string() });

app.post('/restore', (req, res) => {
    const raw = JSON.parse(req.body.data);  // JSON puro, sin ejecucion de funciones
    const { error, value } = schema.validate(raw);
    if (error) return res.status(400).json({ error: 'Datos invalidos' });
    res.json(value);
});
