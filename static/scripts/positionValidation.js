(function () {
                console.log("dom is ready")
                var form = document.querySelector(".need-validation")
                var positionInput = document.getElementById("position")

                console.log(form)
                console.log(positionInput)

                form.addEventListener("submit", evt => {
                    evt.preventDefault()
                    evt.stopPropagation()
                    const validName = validateName(positionInput)

                    if (validName) {
                        form.submit()
                    }
                })

                const validateName = (input) => {
                    if (input.value === "") {
                        showError(input, 'Position is required')
                    } else if (input.value.match(/^[^A-Z]+$/)) {
                        showError(input, 'Continent should be only capital character')
                    } else if (!input.value.match(/^[a-zA-Z]+$/)) {
                        showError(input, 'Continent cannot contain special character')
                    } else if (input.value.length < 2) {
                        showError(input, 'Position should be at least 3 characters long')
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