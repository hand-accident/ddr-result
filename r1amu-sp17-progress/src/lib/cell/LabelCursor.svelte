<script>
    let className;
    export { className as class };
</script>

<!-- svelte-ignore a11y-label-has-associated-control -->
<label class="c {className}"><slot /></label>

<style lang="postcss" module>
    .c {
        @apply cursor-pointer flex select-none items-center justify-between;
    }
</style>
