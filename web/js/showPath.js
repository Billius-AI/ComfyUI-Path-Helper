import {app} from "../../../scripts/app.js";
import {ComfyWidgets} from "../../../scripts/widgets.js";

// Displays input path text on a node
app.registerExtension({
    name: "path_helper.ShowPath",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeType.comfyClass === "Show Path") {
            function populate(text) {
                console.log("sp")
                console.log(this.widgets)
                if (this.widgets) {
                    for (let i = 1; i < this.widgets.length; i++) {
                        this.widgets[i].onRemove?.();
                    }
                    this.widgets.length = 1;
                }

                const v = [...text];
                if (!v[0]) {
                    v.shift();
                }
                for (const list of v) {
                    const w = ComfyWidgets["STRING"](this, "text", ["STRING", {multiline: true}], app).widget;
                    w.inputEl.readOnly = true;
                    w.inputEl.style.opacity = 0.6;
                    w.value = list;
                }

                requestAnimationFrame(() => {
                    const sz = this.computeSize();
                    if (sz[0] < this.size[0]) {
                        sz[0] = this.size[0];
                    }
                    if (sz[1] < this.size[1]) {
                        sz[1] = this.size[1];
                    }
                    this.onResize?.(sz);
                    app.graph.setDirtyCanvas(true, false);
                });
            }

            // When the node is executed we will be sent the input text, display this in the widget
            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                console.log("one")
                onExecuted?.apply(this, arguments);
                populate.call(this, message.text);
            };

            const onConfigure = nodeType.prototype.onConfigure;
            nodeType.prototype.onConfigure = function () {
                onConfigure?.apply(this, arguments);
                if (this.widgets_values?.length) {
                    console.log("eeee")
                    populate.call(this, this.widgets_values);
                }
            };
        }
    },
});

