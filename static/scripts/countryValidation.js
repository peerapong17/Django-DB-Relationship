(function () {
                var form = document.querySelector(".need-validation")
                var countryInput = document.getElementById("country")
                var selectOption = document.getElementById("continent")

                form.addEventListener("submit", evt => {
                    evt.preventDefault()
                    evt.stopPropagation()
                    const validName = validateName(countryInput)
                    const validContinent = validateContinent(selectOption)

                    if (validName && validContinent) {
                        form.submit()
                    }

                })

                const validateName = (input) => {
                    if (input.value == "") {
                        showError(input, 'Country name is required')
                    } else if (!input.value.match(/^[a-zA-Z\s]+$/)) {
                        showError(input, 'Country name cannot contain special character')
                    } else if (input.value.length < 3) {
                        showError(input, 'Continent name should be at least 3 characters long')
                    } else {
                        showSuccess(input)
                        return true
                    }
                }

                const validateContinent = (input) => {
                    if (input.value == "Continent") {
                        showError(input, 'Continent is required')
                    } else {
                        showSuccess(input)
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