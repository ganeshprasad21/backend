Feature('initial task');

Scenario('test google search', ({I}) => {
  I.amOnPage('https://google.com');
  I.fillField({name: 'q'}, 'automation');
  // I.click({name: 'btnK'});
  I.pressKey('Enter');
  setTimeout( () => {console.log("hi")},1000);
  
});

Scenario('alert something', ({I}) => {
  I.amOnPage('https://google.com');
  I.fillField({name: 'q'}, 'ansible');
  // I.click({name: 'btnK'});
  I.pressKey('Enter');
  // setTimeout( () => {prompt("hi")},1000);
  
});