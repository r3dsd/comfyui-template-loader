import { app } from "../../../scripts/app.js";
import { api } from "../../../scripts/api.js";

const cache = {};

async function getKeys(filename) {
    if (caches[filename]) {
        return caches[filename];
    }
    
    const res = await api.fetchApi(`/templates/${filename}`);
    const { keys } = await res.json();
    caches[filename] = keys;
    return caches[filename];
}

app.registerExtension({
    name: "TemplateLoader",
    nodeCreated(node) {
        if (node.comfyClass == "TemplateLoader") {
            const sourceWidget = node.widgets[node.widgets.findIndex(w => w.name == "source")];
            const templateWidget = node.widgets[node.widgets.findIndex(w => w.name == "template")];

            Object.defineProperty(templateWidget.options, "values", {
                set:(x) => {},
                get() {
                    getKeys(sourceWidget.value);
                    return caches[sourceWidget.value];
                }
            });
            
            sourceWidget.callback = async () => {
                const keys = await getKeys(sourceWidget.value);
                Object.defineProperty(templateWidget.options, "values", {
                    set:(x) => {},
                    get() {
                        return keys;
                    }
                });
                node.widgets[1].value = keys[0] || "";
            }
        }
    }
});