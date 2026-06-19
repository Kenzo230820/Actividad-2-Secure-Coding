# src/python/routes/serialize.py
# PASO 4: Insecure Deserialization — usar JSON con schema validado en lugar de pickle
# CODIGO SEGURO
// VULNERABLE — deserializacion directa desde input de usuario
@PostMapping("/restore")
public ResponseEntity<?> restore(@RequestBody byte[] data) throws Exception {
    ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(data));
    Object obj = ois.readObject();  // puede activar gadget chains del classpath
    return ResponseEntity.ok(obj.toString());
}
