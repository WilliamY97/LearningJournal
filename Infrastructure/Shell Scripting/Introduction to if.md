# Introduction to If

http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html

The most compact syntax of the if command is:

```
if TEST-COMMANDS; then CONSEQUENT-COMMANDS; fi
```

Example:

```
if [[ -z "${MODEL_NEEDED}" ]]; then
  # NO MODEL NEEDED, HENCE blank
  "${SCRIPT_LOCATION}/../../contrib/deploy-model.sh" \
    --server-name "${SERVERNAME}" \
    --http-port "${PORT}" \
    --deploy-dir "${DEPLOY_DIR}"
elif [[ "${MODEL_NEEDED}" =~ '\.zip$' ]]; then
  # FROM FILE
  echo TODO - deploy from file
else
  # FROM FOLDER
  echo TODO - deploy from file
fi
```
