
// const dfsPrint = (graph, source) => {
//     const stack = [ source ];
//
//     while (stack.length > 0) {
//         const current = stack.pop();
//         console.log(current);
//
//         for (let neighbor of graph[current]) {
//             stack.push(neighbor);
//         }
//     }
// }

const dfsPrint = (graph, source) => {
    console.log(source);
    for (let neighbor of graph[source]) {
        dfsPrint(graph, neighbor);
    }
}

const bfsPrint = (graph, source) => {
    const q = [ source ];
    while (q.length > 0) {
        const current = q.shift();
        console.log(current);
        for (let neighbor of graph[current]) {
            q.push(neighbor);
        }
    }
}

// const graph = {
//     a: ['b', 'c'],
//     b: ['d'],
//     c: ['e'],
//     d: ['f'],
//     e: [],
//     f: []
// }

const graph = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['j', 'k'],
    j: ['i'],
    k: []
}

// dfsPrint(graph, 'a');
// bfsPrint(graph, 'a');

