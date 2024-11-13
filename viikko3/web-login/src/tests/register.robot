*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  newuser
    Set Password  validPassword1
    Set Password Confirmation  validPassword1
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ne
    Set Password  validPassword1
    Set Password Confirmation  validPassword1
    Submit Registration
    Registration Should Fail With Message  Username must contain only letters a-z and be at least three characters long

Register With Valid Username And Too Short Password
    Set Username  newuser
    Set Password  invalid
    Set Password Confirmation  invalid
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  newuser
    Set Password  invalidPassword
    Set Password Confirmation  invalidPassword
    Submit Registration
    Registration Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  newuser
    Set Password  validPassword1
    Set Password Confirmation  invalidPassword
    Submit Registration
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  validPassword1
    Set Password Confirmation  validPassword1
    Submit Registration
    Registration Should Fail With Message  Username is already in use

*** Keywords ***
Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password   ${password}

Set Password Confirmation
    [Arguments]    ${password_confirmation}
    Input Password    password_confirmation   ${password_confirmation}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page