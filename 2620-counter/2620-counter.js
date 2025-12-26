/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var current = n
    return function() {
        return current++
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */