import { app } from "../../../scripts/app.js";
import { api } from "../../../scripts/api.js";

async function getKeys(filename) {
    const res = await api.fetchApi(`/templates/${filename}`);
    const { keys } = await res.json();
    return keys;
}

app.registerExtension({
    name: "TemplateLoader",
    async nodeCreated(node) {
        const setKeys = async (node) => {
            const keys = await getKeys(node.widgets[0].value);
            Object.defineProperty(node.widgets[1].options, "values", {
                get() {
                    return keys;
                }
            });
        }

        if (node.comfyClass == "TemplateLoader") {
            setKeys(node);
            node.widgets[1].value = "Select the Template.";
            node.widgets[0].callback = async () => {
                const keys = setKeys(node);
                node.widgets[1].value = keys[0] || "";
            }
        }
    }
});