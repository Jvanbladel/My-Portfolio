// Define the grid size
const gridSize = 5;

// Create the grid and add event listeners to each cell
const gridContainer = document.querySelector('.grid-container');
const grid = [];
let misses = 0;
let shipsSunk = 0;
let isGameOver = false;

for (let row = 0; row < gridSize; row++) {
  const rowCells = [];
  for (let col = 0; col < gridSize; col++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.setAttribute('data-row', row);
    cell.setAttribute('data-col', col);
    cell.innerText = '';
    cell.addEventListener('click', shoot);
    rowCells.push(cell);
    gridContainer.appendChild(cell);
  }
  grid.push(rowCells);
}

// Ship data
const ships = [
  { size: 4, name: 'Ship1', number: 1 },
  { size: 3, name: 'Ship2', number: 2 },
  { size: 2, name: 'Ship3', number: 3 }
];

function canPlaceShip(startRow, startCol, size, isVertical) {
    if (isVertical) {
      if (startRow + size > gridSize) {
        return false; // Ship would go out of bounds vertically
      }
      for (let i = 0; i < size; i++) {
        if (grid[startRow + i][startCol].classList.contains('ship')) {
          return false; // Ship would overlap with another ship
        }
      }
    } else {
      if (startCol + size > gridSize) {
        return false; // Ship would go out of bounds horizontally
      }
      for (let i = 0; i < size; i++) {
        if (grid[startRow][startCol + i].classList.contains('ship')) {
          return false; // Ship would overlap with another ship
        }
      }
    }
    return true;
  }
  
  // Function to place ships randomly on the grid
  function placeShipsRandomly() {
    for (const ship of ships) {
      let isVertical, startRow, startCol, canPlaceShipHere;
  
      do {
        isVertical = Math.random() < 0.5;
        if (isVertical) {
          startRow = Math.floor(Math.random() * (gridSize - ship.size + 1));
          startCol = Math.floor(Math.random() * gridSize);
        } else {
          startRow = Math.floor(Math.random() * gridSize);
          startCol = Math.floor(Math.random() * (gridSize - ship.size + 1));
        }
  
        canPlaceShipHere = canPlaceShip(startRow, startCol, ship.size, isVertical);
      } while (!canPlaceShipHere);
  
      // Place the ship on the grid
      for (let i = 0; i < ship.size; i++) {
        if (isVertical) {
          grid[startRow + i][startCol].classList.add('ship');
          grid[startRow + i][startCol].setAttribute('data-ship', ship.number);
        } else {
          grid[startRow][startCol + i].classList.add('ship');
          grid[startRow][startCol + i].setAttribute('data-ship', ship.number);
        }
      }
    }
  }

  function initializeMissesGrid() {
    const missesGrid = document.querySelector('.misses-grid');
    missesGrid.innerHTML = '';
  
    for (let i = 0; i < 10; i++) {
      const missCell = document.createElement('div');
      missCell.classList.add('miss-cell');
      missesGrid.appendChild(missCell);
    }
  }
  
  // Function to update the misses grid after each miss
  function updateMissesGrid() {
    const missesGrid = document.querySelector('.misses-grid');
    const missCells = missesGrid.querySelectorAll('.miss-cell');
  
    for (let i = 0; i < misses; i++) {
      missCells[i].textContent = 'M';
    }
  }

// Function to handle shooting at a cell
function shoot(event) {
    if (isGameOver) {
      return; // Prevent further actions if the game is already over
    }
  
    const cell = event.target;
    const row = cell.getAttribute('data-row');
    const col = cell.getAttribute('data-col');
  
    if (cell.classList.contains('hit')) {
      return; // Cell already hit, do nothing
    }
  
    if (cell.classList.contains('ship')) {
      const shipNumber = cell.getAttribute('data-ship');
      cell.innerText = 'H'; // Display "H" for a hit
      cell.classList.add('hit');
      checkSunkShips(row, col, shipNumber);
    } else {
      cell.innerText = 'M'; // Missed the ship
      cell.classList.add('hit');
      misses++;
      updateMissesCounter();
      updateMissesGrid(); // Update the misses grid after each miss
    }
  
    cell.removeEventListener('click', shoot);
    checkGameOver(); // Check if the game is over after each shot
  }

// Function to check if any ship is sunk after a hit
function checkSunkShips(row, col, shipNumber) {
    const shipCells = Array.from(document.querySelectorAll(`[data-ship="${shipNumber}"]`));
    const isVertical = shipCells[0].getAttribute('data-row') !== shipCells[1].getAttribute('data-row');
    let allShipCellsHit = true; // Assume all cells are hit until proven otherwise
  
    for (const cell of shipCells) {
      if (!cell.classList.contains('hit')) {
        allShipCellsHit = false;
        break; // The ship is not yet sunk, exit the loop
      }
    }
  
    if (allShipCellsHit) {
      // If all cells of the ship are hit, mark it as sunk
      for (const cell of shipCells) {
        cell.innerText = shipNumber;
      }
  
      // Remove the ship number from the hit cells to avoid confusion
      for (const cell of shipCells) {
        cell.removeAttribute('data-ship');
      }
  
      shipsSunk++;
      updateShipsSunkCounter();
    }
  }

// Function to update the misses counter
function updateMissesCounter() {
    console.log('Misses:', misses);
  }
  
  // Function to update the ships sunk counter
  function updateShipsSunkCounter() {
    console.log('Ships Sunk:', shipsSunk);
  }

// Function to check if the game is over
function checkGameOver() {
    if (shipsSunk === ships.length) {
      endGame("You Win!"); // All ships are sunk, end the game
    } else if (misses >= 10) {
      endGame("Game Over! You Lost."); // Player lost due to too many misses
    }
  }
  
  // Function to end the game
  function endGame(message) {
    console.log('Game Over:', message);
    isGameOver = true;
    setTimeout(() => {
      alert(message);
      const resetBtn = document.getElementById('resetBtn');
      resetBtn.style.display = 'block';
    }, 100); // Delay the alert by 100 milliseconds to allow the board to update
  }
  
  // Function to reset the game
  function resetGame() {
    location.reload(); // Reload the page to reset the game
  }
  
// Function to hide the reset button
function hideResetButton() {
    const resetBtn = document.getElementById('resetBtn');
    resetBtn.style.display = 'none';
  }
  // Function to end the game and show the reset button
  // Add event listener to the reset button
  const resetBtn = document.getElementById('resetBtn');
    resetBtn.addEventListener('click', resetGame);
  
  // ... (existing code)
  
  // Place ships randomly at the beginning of the game
  initializeMissesGrid();
  placeShipsRandomly();