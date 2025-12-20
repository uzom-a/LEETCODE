/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(){
        return "Hello World";
    }  
    
};

// console.log(createHelloWorld)

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */