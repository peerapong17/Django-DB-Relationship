(function () {
                var form = document.querySelector(".need-validation")
                var nameInput = document.getElementById("name")
                var ageInput = document.getElementById("age")
                var countrySelect = document.getElementById("country")
                var clubSelect = document.getElementById("club")
                var positionContainer = document.getElementById("positionContainer")
                var positionList = document.querySelectorAll("#positions")

                form.addEventListener("submit", evt => {
                    evt.preventDefault()
                    evt.stopPropagation()

                    const validName = validateName(nameInput)
                    const validAge = validateAge(ageInput)
                    const validCountry = validateSelect(countrySelect, "Country")
                    const validClub = validateSelect(clubSelect, "Club")
                    const validPosition = validatePosition(positionContainer.children[12])

                    if (validName && validAge && validCountry && validClub && validPosition) {
                        form.submit()
                    }
                })

                const validateName = (input) => {
                    if (input.value == "") {
                        showError(input, 'Name is required')
                    } else if (!input.value.match(/^[a-zA-Z\s]+$/)) {
                        showError(input, 'Name cannot contain special character')
                    } else if (input.value.length < 3) {
                        showError(input, 'Name should be at least 3 characters long')
                    } else {
                        showSuccess(input)
                        return true
                    }
                }

                const validateAge = (input) => {
                    if (input.value == "") {
                        showError(input, 'Age is required')
                    } else if (input.value < 0) {
                        showError(input, 'Age cannot be lower than 0')
                    } else {
                        showSuccess(input)
                        return true
                    }
                }
                const validateSelect = (input, baseType) => {
                    if (input.value == baseType) {
                        showError(input, 'Continent is required')
                    } else {
                        showSuccess(input)
                        return true
                    }
                }

                const validatePosition = (input) => {
                    var positionIds = []
                    positionList.forEach(position => {
                        if (position.checked == true) {
                            positionIds.push(position.checked)
                        }
                    })
                    if (positionIds.length == 0) {
                        input.classList.remove("d-none")
                        input.classList.add("d-block")
                        input.innerHTML = 'Player should have at least 1 position'
                    } else {
                        input.classList.remove("d-block")
                        input.classList.add("d-none")
                        input.innerHTML = ""
                        return true
                    }
                }

                const showError = (input, message) => {
                    input.classList.remove("is-valid")
                    input.classList.add("is-invalid")
                    input.nextSibling.nextSibling.innerHTML = message
                }

                const showSuccess = (input) => {
                    input.classList.remove("is-invalid")
                    input.classList.add("is-valid")
                }

            }
        )()