(function () {
                console.log("dom is ready")
                var form = document.querySelector(".need-validation")
                var continentInput = document.getElementById("continent")

                form.addEventListener("submit", evt => {
                    evt.preventDefault()
                    evt.stopPropagation()
                    const validName = validateName(continentInput)

                    if(validName){
                        form.submit()
                    }
                })

                const validateName = (input) => {
                    if (input.value === "") {
                        showError(input, 'Continent name is required')
                    } else if (!input.value.match(/^[a-zA-Z\s]+$/)) {
                        showError(input, 'Continent cannot contain special character')
                    } else if (input.value.length < 3) {
                        showError(input, 'Continent name should be at least 3 characters long')
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