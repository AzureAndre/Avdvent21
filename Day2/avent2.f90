program atom_test

    implicit none
    integer :: ios
    integer, parameter :: read_unit = 99
    character(len=200) :: command(3000)
    integer :: n, i

    open(unit=read_unit, file='data.dat', iostat=ios)
    if ( ios /= 0 ) stop "Error opening file data.dat"

    n = 0

    do
        read(read_unit, '(A)', iostat=ios) command(n+1)
        if (ios /= 0) exit
        n = n + 1
    end do

    print*, "File contains ", n, "commands"

    close(read_unit)

    do i = 1, n
        print*, command(i)
    end do

end program atom_test