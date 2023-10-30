/// <reference types="cypress"/>



describe('Criando cenário de teste para o site gobalsqa', () => {

  it.skip('Registrar usuario', () => { 

      cy.visit('https://globalsqa.com/angularJs-protractor/registration-login-example/#/login')
      cy.get('.btn-link').click()
      cy.get('#firstName').type('Inatel')
      cy.get('#Text1').type('inatel')
      cy.get('#username').type('inatel')
      cy.get('#password').type('inatel')
      cy.get('.btn-primary').click()
      cy.get('.ng-binding').should('contain.text','Registration successful')

  });
  
  it.skip('realizar login com exito', () => { 

      cy.visit('https://globalsqa.com/angularJs-protractor/registration-login-example/#/register')
      cy.get('#firstName').type('Inatel')
      cy.get('#Text1').type('inatel')
      cy.get('#username').type('inatel')
      cy.get('#password').type('inatel')
      cy.get('#password').clear()
      cy.get('.has-error > .help-block').should('have.text', 'Password is required')
      cy.get('.btn-primary').should('be.disabled')
  });

  it('registrar e logar com exito no site', () => { 
      
      let info = registrarUSUARIO()
      cy.get('#username').type(info[0])
      cy.get('#password').type(info[1])
      cy.get('.btn-primary').click()
      cy.get('.btn-primary').should('not.contain.text',info[0])
  });

});

function registrarUSUARIO(){

  let horas = new Date().getHours().toString()
  let minutos = new Date().getMinutes().toString()
  let seg = new Date().getSeconds().toString()
  let user = horas + minutos + seg + 'Id'
  let senha = horas + minutos + seg + 'senha'
  let userInfo = [user,senha]

  cy.visit('https://globalsqa.com/angularJs-protractor/registration-login-example/#/login')
  cy.get('.btn-link').click()
  cy.get('#firstName').type(user)
  cy.get('#Text1').type(user)
  cy.get('#username').type(user)
  cy.get('#password').type(senha)
  cy.get('.btn-primary').click()
  cy.get('.ng-binding').should('contain.text','Registration successful')

  return userInfo
}
