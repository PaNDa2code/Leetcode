var countNegatives = function(grid) {
    let x;
    let neg = 0
    for(x = 0;x < grid.length;x++){
        
        let y;
        for(y = 0; y < grid[x].length; y++){
            if (grid[x][y] < 0){
                neg ++
            }
        }
        
    };
    
    return neg
    
};