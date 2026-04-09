function simple_topo_sort(steps, dependencies) {
    const ordered = [];
    const remaining = [...steps];

    while (remaining.length > 0) {
        for (let i = 0; i < remaining.length; i++) {
            const step = remaining[i];
            // console.log(`Adding step: ${step}`);
            // Check if all dependencies are satisfied
            if (dependencies.every(([pre, post]) => post !== step || ordered.includes(pre))) {
                ordered.push(step);
                // console.log(`Ordered: ${JSON.stringify(ordered)}`);
                remaining.splice(i, 1);
                break;
            }
        }
    }

    return ordered;
}

const steps = [
    "włącz czajnik",
    "włóż herbatę do kubka",
    "wyjmij kubek",
    "zalej herbatę",
    "znajdź opakowanie herbaty",
    "nalej wody do czajnika",
];

const dependencies = [
    ["włóż herbatę do kubka", "zalej herbatę"],
    ["wyjmij kubek", "włóż herbatę do kubka"],
    ["znajdź opakowanie herbaty", "włóż herbatę do kubka"],
    ["nalej wody do czajnika", "włącz czajnik"],
    ["włącz czajnik", "zalej herbatę"],
];

console.log(simple_topo_sort(steps, dependencies));