<script>
    import DrawerBody from "../cell/DrawerBody.svelte";
    import DrawerContent from "../cell/DrawerContent.svelte";
    import DrawerEnd from "../cell/DrawerEnd.svelte";
    import DrawerOverlayGlass from "../cell/DrawerOverlayGlass.svelte";
    import DrawerSide from "../cell/DrawerSide.svelte";
    import DrawerToggle from "../cell/DrawerToggle.svelte";

    let checked = false;
</script>

<DrawerEnd class="">
    <DrawerToggle id="config" class="" bind:checked />
    <DrawerContent class="l0" {checked}>
        <slot name="content" />
    </DrawerContent>
    <DrawerSide class="" {checked}>
        <DrawerOverlayGlass class="" {checked} for="config" />
        <DrawerBody {checked} class="l1">
            <slot name="drawer" />
        </DrawerBody>
    </DrawerSide>
</DrawerEnd>

<style lang="postcss" module>
    .l0 {
        @apply h-screen flex flex-col;
    }
    .l1 {
        @apply flex flex-col gap-1 p-4;
    }
</style>
