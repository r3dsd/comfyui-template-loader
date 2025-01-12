import { app } from "../../../scripts/app.js";
import { api } from "../../../scripts/api.js";

const cache = {};

async function getKeys(filename) {
    if (cache[filename]) {
        return cache[filename];
    }
    
    const res = await api.fetchApi(`/templates?name=${filename}`);
    const { keys } = await res.json();
    cache[filename] = keys;
    return cache[filename];
}

app.registerExtension({
    name: "TemplateLoader",
    nodeCreated(node) {
        if (node.comfyClass == "TemplateLoader") {
            const sourceWidget = node.widgets[node.widgets.findIndex(w => w.name == "source")];
            const templateWidget = node.widgets[node.widgets.findIndex(w => w.name == "template")];

            sourceWidget.callback = async () => {
                await getKeys(sourceWidget.value);
                Object.defineProperty(templateWidget.options, "values", {
                    get() {
                        return cache[sourceWidget.value];
                    },
                });
                templateWidget.value = cache[sourceWidget.value][0];
            };
        }
    },
    async afterConfigureGraph() {
        const nodes = app.graph.nodes.filter(node => node.comfyClass === "TemplateLoader");
        for (const node of nodes) {
            const sourceWidget = node.widgets[node.widgets.findIndex(w => w.name == "source")];
            const templateWidget = node.widgets[node.widgets.findIndex(w => w.name == "template")];

            Object.defineProperty(templateWidget.options, "values", {
                set: (x) => {},
                get() {
                    getKeys(sourceWidget.value);
                    return cache[sourceWidget.value];
                },
            });
        }
    },
});